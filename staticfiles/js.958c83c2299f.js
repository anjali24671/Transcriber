function copyToClipboard(){
    // Copy to clipboard
    let text_para = document.querySelector(".text-box").innerText
    navigator.clipboard.writeText(text_para);

    // Change the text of button to copied
    document.querySelector('.copy-button').innerText = "Copied!"
    
}