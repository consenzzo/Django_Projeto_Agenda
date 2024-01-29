var formToDelete;
        
function showModal(form) {
    formToDelete = form;
    document.getElementById('deleteConfirmModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('deleteConfirmModal').style.display = 'none';
}

function confirmDeletion() {
    closeModal();
    formToDelete.submit();
}