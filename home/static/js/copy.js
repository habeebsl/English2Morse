document.addEventListener('DOMContentLoaded', () => {

    const button = document.getElementsByName('copyButton')[0];
    const paragraph = document.querySelector('.content p'); 

    button.addEventListener('click', () => {
        const paragraphContent = paragraph.textContent;

        if (navigator.clipboard) {
            navigator.clipboard.writeText(paragraphContent)
                .then(() => {
                    console.log('Text copied to clipboard successfully');
                    button.textContent = 'Copied';
                })
                .catch((error) => {
                    console.error('Unable to copy text to clipboard:', error);
                });
        } else {
            console.warn('Clipboard API not supported');
        }
    });
});
