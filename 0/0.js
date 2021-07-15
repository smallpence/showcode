/**
 * 
 * @param {string} message 
 */
function halliday(message) {
    return message.split("")
        .map(char => char.charCodeAt(0))
        .map(num => {
            if (num >= 65 && num <= 90) {
                num -= 13;
                if (num < 65) num += 26;
                return num;
            }

            if (num >= 97 && num <= 122) {
                num -= 13;
                if (num < 97) num += 26;
                return num;
            }

            return num;
        })
        .map(num => String.fromCharCode(num))
        .join("");
};

console.log(halliday("Crystal Key"));