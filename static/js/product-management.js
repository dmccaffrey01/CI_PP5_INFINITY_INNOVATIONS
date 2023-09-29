const newImageInput = document.querySelector('#new_image');
const fileName = document.querySelector('#filename');

newImageInput.addEventListener('change', () => {
    let file = newImageInput.files[0];
    fileName.innerText = `Image will be set to: ${file.name}`;
});