document.addEventListener('DOMContentLoaded', () => {
    const addPostIcon = document.querySelector('.header-icons img[src*="plus.svg"]');
    const createPostModal = document.querySelector('.create-post-modal');
    const closeModal = document.querySelector('.close-modal');

    // Show modal when plus icon is clicked
    addPostIcon.addEventListener('click', () => {
        createPostModal.style.display = 'block';
    });

    // Close modal
    closeModal.addEventListener('click', () => {
        createPostModal.style.display = 'none';
    });
});