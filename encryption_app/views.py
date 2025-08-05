from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from .models import Channel, ChannelMembership, EncryptedMessage
from .forms import SignUpForm, ChannelCreateForm, ChannelJoinForm, EncryptForm, DecryptForm
from .utils import full_encrypt, full_decrypt, parse_secret_key_input
import json


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')


@login_required
def dashboard(request):
    user_channels = Channel.objects.filter(
        channelmembership__user=request.user
    ).distinct()

    context = {
        'user_channels': user_channels,
        'total_channels': user_channels.count(),
    }
    return render(request, 'dashboard.html', context)


@method_decorator(csrf_protect, name='dispatch')
class ChannelCreateView(LoginRequiredMixin, CreateView):
    model = Channel
    form_class = ChannelCreateForm
    template_name = 'channel_create.html'

    def form_valid(self, form):
        channel = form.save(commit=False)
        channel.creator = self.request.user

        # Generate and set custom map
        custom_map = channel.generate_default_map()
        channel.set_custom_map(custom_map)

        channel.save()

        # Add creator as member
        ChannelMembership.objects.create(
            user=self.request.user,
            channel=channel
        )

        messages.success(self.request, f'Channel "{channel.name}" created successfully!')
        return redirect('dashboard')


@login_required
@csrf_protect
def channel_join(request):
    if request.method == 'POST':
        form = ChannelJoinForm(request.POST)
        if form.is_valid():
            channel_key = form.cleaned_data['channel_key']
            try:
                channel = Channel.objects.get(key=channel_key)
                membership, created = ChannelMembership.objects.get_or_create(
                    user=request.user,
                    channel=channel
                )

                if created:
                    messages.success(request, f'Successfully joined channel "{channel.name}"!')
                else:
                    messages.info(request, f'You are already a member of "{channel.name}".')

                return redirect('dashboard')
            except Channel.DoesNotExist:
                messages.error(request, 'Invalid channel key.')
    else:
        form = ChannelJoinForm()

    return render(request, 'channel_join.html', {'form': form})


@login_required
@csrf_protect
def encrypt_message(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)

    # Check if user is member
    if not ChannelMembership.objects.filter(user=request.user, channel=channel).exists():
        messages.error(request, 'You are not a member of this channel.')
        return redirect('dashboard')

    if request.method == 'POST':
        form = EncryptForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']

            # Encrypt the message
            encrypted_result = full_encrypt(message, channel)

            if isinstance(encrypted_result, str):
                messages.error(request, f'Encryption error: {encrypted_result}')
            else:
                # Save encrypted message
                EncryptedMessage.objects.create(
                    encrypted_data=json.dumps(encrypted_result),
                    channel=channel,
                    created_by=request.user
                )

                context = {
                    'channel': channel,
                    'original_message': message,
                    'encrypted_result': encrypted_result,
                    'form': EncryptForm()
                }
                return render(request, 'encrypt.html', context)
    else:
        form = EncryptForm()

    return render(request, 'encrypt.html', {'form': form, 'channel': channel})


@login_required
@csrf_protect
def decrypt_message(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)

    # Check if user is member
    if not ChannelMembership.objects.filter(user=request.user, channel=channel).exists():
        messages.error(request, 'You are not a member of this channel.')
        return redirect('dashboard')

    if request.method == 'POST':
        form = DecryptForm(request.POST)
        if form.is_valid():
            secret_key_input = form.cleaned_data['secret_key']

            # Parse secret key
            parsed_key = parse_secret_key_input(secret_key_input)

            if parsed_key is None:
                messages.error(request, 'Invalid secret key format!')
            else:
                # Decrypt the message
                decrypted_result = full_decrypt(parsed_key, channel)

                context = {
                    'channel': channel,
                    'secret_key': parsed_key,
                    'decrypted_result': decrypted_result,
                    'form': DecryptForm()
                }
                return render(request, 'decrypt.html', context)
    else:
        form = DecryptForm()

    return render(request, 'decrypt.html', {'form': form, 'channel': channel})


@login_required
def channel_messages(request, channel_id):
    channel = get_object_or_404(Channel, id=channel_id)

    # Check if user is member
    if not ChannelMembership.objects.filter(user=request.user, channel=channel).exists():
        messages.error(request, 'You are not a member of this channel.')
        return redirect('dashboard')

    messages = EncryptedMessage.objects.filter(channel=channel)[:50]

    return render(request, 'channel_messages.html', {
        'channel': channel,
        'messages': messages
    })


class HelpView(TemplateView):
    template_name = 'help.html'