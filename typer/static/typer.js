let typeHereInput = document.getElementById("type-here")
let nextLineId = document.getElementById("next-line-id").value
let currentLineTypedElement = document.getElementById("line-current-typed")
let currentLineWronglyTypedElement = document.getElementById("line-current-wrongly-typed")
let currentLineElement = document.getElementById("line-current-to-type")
let currentLine = document.getElementById("line-current-to-type").innerHTML
let typedText = ""
console.log({currentLine})

//typeHereInput.addEventListener("oninput", handleOnChange);
//typeHereInput.addEventListener("keyup", handleOnChange);


function handleOnChange(){
    let typedText = typeHereInput.value
    let maxMatch = 0;

    // Redirect to next text if the current text is good and submit the score
    if (typedText.substring(0, currentLine.length) == currentLine) {
        console.log({currentLine, nextLineId})
        if (nextLineId) {
            window.location.href = "/text/" + nextLineId
        } else {
            window.location.href = "/"
        }
        return
    }

    // Fill spans if typedText is good
    let curLineSubstr = currentLine.substring(0, typedText.length)
    console.log({curLineSubstr, typedText})
    if (curLineSubstr == typedText) {
        currentLineTypedElement.innerHTML = currentLine.substring(0, typedText.length);
        currentLineElement.innerHTML = currentLine.substring(typedText.length);
        currentLineWronglyTypedElement.innerHTML = ""
        typeHereInput.classList.remove('error')
        return;
    }

    // Find the index of the last correct character
    let correctIndex = 0;
    for (let i = 0; i < typedText.length; i++) {
        if (typedText[i] == currentLine[i]) {
            correctIndex++
        } else {
            break;
        }
    }
    // Fill the currentLine spans
    currentLineTypedElement.innerHTML = currentLine.substring(0, correctIndex);
    currentLineWronglyTypedElement.innerHTML = currentLine.substring(correctIndex, typedText.length);
    currentLineElement.innerHTML = currentLine.substring(typedText.length);
    typeHereInput.classList.add('error')

    console.log({typedText, correctIndex})
}