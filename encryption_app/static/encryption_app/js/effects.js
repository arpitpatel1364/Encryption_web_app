document.addEventListener('DOMContentLoaded', () => {
    // Glitch Effect for Titles
    const glitchElements = document.querySelectorAll('.navbar-brand, .terminal-title, .result-title');
    glitchElements.forEach(el => {
        el.setAttribute('data-text', el.textContent);
        el.addEventListener('mouseover', () => {
            el.classList.add('glitch');
            setTimeout(() => el.classList.remove('glitch'), 1000);
        });
    });

    // Typing Animation for Terminal
    const terminal = document.querySelector('.status-terminal');
    if (terminal) {
        const messages = [
            'Initializing neural network...',
            'Quantum encryption protocols engaged.',
            'Data stream integrity: 98.7%',
            'System diagnostics complete.'
        ];
        let messageIndex = 0;
        let charIndex = 0;
        let currentMessage = '';

        function type() {
            if (charIndex < messages[messageIndex].length) {
                currentMessage += messages[messageIndex].charAt(charIndex);
                terminal.textContent = currentMessage + '_';
                charIndex++;
                setTimeout(type, 100);
            } else {
                setTimeout(() => {
                    charIndex = 0;
                    currentMessage = '';
                    messageIndex = (messageIndex + 1) % messages.length;
                    type();
                }, 2000);
            }
        }
        type();
    }

    // Plasma Energy Effect on Buttons
    const buttons = document.querySelectorAll('.terminal-btn, .btn, .floating-button');
    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            btn.style.animation = 'plasma 0.5s ease';
            setTimeout(() => {
                btn.style.animation = '';
            }, 500);
        });
    });

    // Digital Corruption Effect on Text Inputs
    const textInputs = document.querySelectorAll('.form-control, .terminal-input');
    textInputs.forEach(input => {
        input.addEventListener('input', () => {
            if (Math.random() > 0.8) {
                input.classList.add('glitch');
                setTimeout(() => input.classList.remove('glitch'), 300);
            }
        });
    });

    // Streaming Data Background Effect
    function createDataStream() {
        const stream = document.createElement('div');
        stream.className = 'data-stream';
        stream.style.position = 'fixed';
        stream.style.top = '0';
        stream.style.left = `${Math.random() * 100}%`;
        stream.style.width = '2px';
        stream.style.height = '100%';
        stream.style.background = 'linear-gradient(to bottom, transparent, var(--neon-green))';
        stream.style.opacity = '0.3';
        stream.style.animation = 'stream 5s linear';
        document.body.appendChild(stream);
        setTimeout(() => stream.remove(), 5000);
    }
    setInterval(createDataStream, 1000);

    // System Diagnostic Animation for Progress Indicator
    const progress = document.querySelector('.progress-indicator');
    if (progress) {
        let width = 0;
        function updateProgress() {
            width = (width + 10) % 110;
            progress.style.width = `${width}%`;
            setTimeout(updateProgress, 200);
        }
        updateProgress();
    }

    // Electromagnetic Interference on Critical Actions
    function triggerEMI() {
        const overlay = document.createElement('div');
        overlay.style.position = 'fixed';
        overlay.style.inset = '0';
        overlay.style.background = 'radial-gradient(circle, rgba(0,255,65,0.1), transparent)';
        overlay.style.opacity = '0';
        overlay.style.animation = 'emi 0.5s ease';
        document.body.appendChild(overlay);
        setTimeout(() => overlay.remove(), 500);
    }

    document.querySelectorAll('.btn-encrypt, .btn-decrypt').forEach(btn => {
        btn.addEventListener('click', triggerEMI);
    });

    // File Upload Zone Feedback
    const fileUpload = document.querySelector('.file-upload');
    if (fileUpload) {
        fileUpload.addEventListener('dragover', () => {
            fileUpload.style.borderColor = 'var(--hot-pink)';
            fileUpload.style.boxShadow = '0 0 20px var(--glow-pink)';
        });
        fileUpload.addEventListener('dragleave', () => {
            fileUpload.style.borderColor = 'var(--electric-blue)';
            fileUpload.style.boxShadow = 'var(--glow-shadow)';
        });
        fileUpload.addEventListener('drop', () => {
            fileUpload.style.animation = 'pulse 0.5s ease';
            setTimeout(() => fileUpload.style.animation = '', 500);
        });
    }

    // Neural Network Connection Lines
    function drawNeuralLines() {
        const canvas = document.createElement('canvas');
        canvas.style.position = 'fixed';
        canvas.style.inset = '0';
        canvas.style.pointerEvents = 'none';
        canvas.style.opacity = '0.2';
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        document.body.appendChild(canvas);
        const ctx = canvas.getContext('2d');
        const elements = document.querySelectorAll('.input-panel, .control-panel, .output-panel');
        elements.forEach(el => {
            const rect = el.getBoundingClientRect();
            const x = rect.left + rect.width / 2;
            const y = rect.top + rect.height / 2;
            ctx.beginPath();
            ctx.moveTo(x, y);
            elements.forEach(other => {
                if (el !== other) {
                    const otherRect = other.getBoundingClientRect();
                    const ox = otherRect.left + otherRect.width / 2;
                    const oy = otherRect.top + otherRect.height / 2;
                    ctx.lineTo(ox, oy);
                    ctx.strokeStyle = 'var(--neon-green)';
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
            });
        });
        setTimeout(() => canvas.remove(), 2000);
    }
    setInterval(drawNeuralLines, 3000);

    // Biometric Scanning Animation
    function biometricScan() {
        const scan = document.createElement('div');
        scan.style.position = 'fixed';
        scan.style.inset = '0';
        scan.style.background = 'linear-gradient(to bottom, transparent, var(--electric-blue) 50%, transparent)';
        scan.style.opacity = '0.3';
        scan.style.animation = 'scan 1s ease';
        document.body.appendChild(scan);
        setTimeout(() => scan.remove(), 1000);
    }

    document.querySelectorAll('.btn-generate-key').forEach(btn => {
        btn.addEventListener('click', biometricScan);
    });

    // Additional CSS for Dynamic Effects
    const style = document.createElement('style');
    style.textContent = `
        @keyframes stream {
            0% { transform: translateY(-100%); opacity: 0; }
            50% { opacity: 0.3; }
            100% { transform: translateY(100%); opacity: 0; }
        }
        @keyframes emi {
            0% { opacity: 0; }
            50% { opacity: 0.3; }
            100% { opacity: 0; }
        }
        @keyframes scan {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(100%); }
        }
    `;
    document.head.appendChild(style);
});