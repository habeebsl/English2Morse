document.addEventListener('DOMContentLoaded', () => {
    // Your code here

    const button = document.getElementsByName('copyButton')[0]; // Assuming there's only one element with the name 'copyButton'
    const paragraph = document.querySelector('.content p'); // Assuming the paragraph is inside an element with class 'content'

    // Add an event listener for the 'click' event
    button.addEventListener('click', () => {
        // Get the value from the input field
        const paragraphContent = paragraph.textContent;

        if (navigator.clipboard) {
            // Attempt to write text to the clipboard
            navigator.clipboard.writeText(paragraphContent)
                .then(() => {
                    console.log('Text copied to clipboard successfully');
                    // Change the button text to 'Copied'
                    button.textContent = 'Copied';
                })
                .catch((error) => {
                    console.error('Unable to copy text to clipboard:', error);
                });
        } else {
            // Fallback for browsers that do not support the Clipboard API
            console.warn('Clipboard API not supported');
        }
    });
});
