const typeWriterText = [
    "Unmatched Quality, Unbeatable Experience!", 
    "Elevate Your Metaverse Journey!",
    "Explore Our Premium Selection Today!"
]

let clearTypewriterText = (i) => {
    const typeWriterTextElement = document.querySelector("#typewriter-text");
    let text = typeWriterText[i];
    let textLength = text.length;

    let clearTextCounter = 0;

    let clearTypewriterInterval = window.setInterval(() => {

        if (clearTextCounter >= textLength - 1) {
            typeWriterTextElement.innerText = "";
            clearInterval(clearTypewriterInterval);
        } else {
            let newText = text.slice(0, -1);

            typeWriterTextElement.innerText = newText;

            text = newText;

            clearTextCounter++;
        }
    }, 10);
}

let typewriterCount = 0;
let typewriterOn = false;
let typewriterOnFirstTime = true;
let waitTime = 5500;

const typewriter = () => {
    const typeWriterTextElement = document.querySelector("#typewriter-text");

    if (typewriterOnFirstTime) {
        typewriterOnFirstTime = false;

        let currentText = typeWriterText[typewriterCount];

        typewriterCount++;

        let letters = currentText.split("");
        
        let lettersLength = letters.length;

        let totalTime = lettersLength * 60;

        let totalClearTime = lettersLength * 10;

        let clearWaitTime = waitTime - (totalTime + totalClearTime + 1200);

        let letterCount = 0;

        let typewriterInterval = window.setInterval(() => {
            if (letterCount > lettersLength - 1) {
                window.setTimeout(() => {
                    clearTypewriterText(typewriterCount - 1);
                }, clearWaitTime);
                
                clearInterval(typewriterInterval);
            } else {
                if (letters[letterCount - 1] == " ") {
                    typeWriterTextElement.innerText += " " + letters[letterCount];
                } else {
                    typeWriterTextElement.innerText += letters[letterCount];
                }
                letterCount++;
            }
        }, 60);
    }

    typewriterOn = true;
    let typewriterOnInverval = window.setInterval(() => {
        if (!typewriterOn) {
            clearInterval(typewriterOnInverval);
        } else {
            let currentText = typeWriterText[typewriterCount];

            let letters = currentText.split("");
            
            let lettersLength = letters.length;

            let totalTime = lettersLength * 60;

            let totalClearTime = lettersLength * 10;

            let clearWaitTime = waitTime - (totalTime + totalClearTime + 1200);

            let t1 = waitTime - (totalTime + totalClearTime)

            let letterCount = 0;

            let typewriterInterval = window.setInterval(() => {
                if (letterCount > lettersLength - 1) {
                    window.setTimeout(() => {
                        let i = typewriterCount;
                        if (i == 0) {
                            i = 3;
                        }
                        clearTypewriterText(i - 1);
                    }, clearWaitTime);
                    typewriterCount++;
                    if (typewriterCount == 3) {
                        typewriterCount = 0;
                    }


                    
                    clearInterval(typewriterInterval);
                } else {
                    if (letters[letterCount - 1] == " ") {
                        typeWriterTextElement.innerText += " " + letters[letterCount];
                    } else {
                        typeWriterTextElement.innerText += letters[letterCount];
                    }
                    letterCount++;
                }
            }, 60);
        }
        
    }, waitTime);
}

document.addEventListener('DOMContentLoaded', () => {
    typewriter();
});