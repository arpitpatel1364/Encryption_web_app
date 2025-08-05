document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('qr-video');
    const canvasElement = document.getElementById('qr-canvas');
    const canvas = canvasElement.getContext('2d');
    const startButton = document.getElementById('start-qr');
    const stopButton = document.getElementById('stop-qr');
    const channelKeyInput = document.getElementById('channel-key-input');
    const beepSound = document.getElementById('beep-sound');

    let scanning = false;

    startButton.addEventListener('click', () => {
        navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
            .then(stream => {
                scanning = true;
                video.srcObject = stream;
                video.style.display = 'block';
                canvasElement.style.display = 'none';
                video.play();
                requestAnimationFrame(tick);
                beepSound.play();
            })
            .catch(err => {
                console.error('Camera access error:', err);
                alert('Unable to access camera. Please ensure camera permissions are granted.');
            });
    });

    stopButton.addEventListener('click', () => {
        if (video.srcObject) {
            video.srcObject.getTracks().forEach(track => track.stop());
            video.style.display = 'none';
            canvasElement.style.display = 'block';
            scanning = false;
            beepSound.play();
        }
    });

    function tick() {
        if (!scanning) return;

        if (video.readyState === video.HAVE_ENOUGH_DATA) {
            canvasElement.height = video.videoHeight;
            canvasElement.width = video.videoWidth;
            canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);
            const imageData = canvas.getImageData(0, 0, canvasElement.width, canvasElement.height);
            const code = jsQR(imageData.data, imageData.width, imageData.height, {
                inversionAttempts: 'dontInvert',
            });

            if (code) {
                channelKeyInput.value = code.data;
                video.srcObject.getTracks().forEach(track => track.stop());
                video.style.display = 'none';
                canvasElement.style.display = 'block';
                scanning = false;
                beepSound.play();
                return;
            }
        }
        requestAnimationFrame(tick);
    }

    // QR Code Generation for Channels
    const qrButtons = document.querySelectorAll('.qr-btn');
    qrButtons.forEach(button => {
        button.addEventListener('click', () => {
            const key = button.getAttribute('data-key');
            const qrContainer = document.getElementById(`qr-${button.closest('.channel-card').querySelector('.qr-code').id.split('-')[1]}`);
            qrContainer.style.display = 'block';
            qrContainer.innerHTML = '';
            new QRCode(qrContainer, {
                text: key,
                width: 128,
                height: 128,
                colorDark: '#05d9e8',
                colorLight: '#0d0d1a',
            });
            beepSound.play();
        });
    });

    // Copy Button Functionality
    const copyButtons = document.querySelectorAll('.copy-btn');
    copyButtons.forEach(button => {
        button.addEventListener('click', () => {
            const text = button.getAttribute('data-key');
            navigator.clipboard.writeText(text);
            alert('Copied to clipboard!');
            beepSound.play();
        });
    });
});