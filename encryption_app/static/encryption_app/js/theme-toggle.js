document.addEventListener('DOMContentLoaded', () => {
    const toggleSwitch = document.querySelector('.theme-switcher input[type="checkbox"]');
    const clickSound = document.getElementById('click-sound');
    const glitchSound = document.getElementById('glitch-sound');
    const ambientSound = document.getElementById('ambient-sound');

    // Play ambient sound on page load
    ambientSound.play().catch(() => console.log('Ambient sound blocked by browser'));

    const currentTheme = localStorage.getItem('theme') || 'cyberpunk';
    document.documentElement.setAttribute('data-theme', currentTheme);
    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
    }

    toggleSwitch.addEventListener('change', (e) => {
        clickSound.play();
        if (e.target.checked) {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'cyberpunk');
            localStorage.setItem('theme', 'cyberpunk');
            glitchSound.play();
        }
    });

    // Add click sound to all buttons
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', () => {
            clickSound.play();
        });
    });
});