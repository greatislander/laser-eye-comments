/**
 * Converts a string to Morse Code.
 *
 * @param {String} str The string to be converted to Morse Code.
 * @returns {String} The string as Morse Code.
 */
function convertToMorseCode(str) {
    // See https://en.wikipedia.org/wiki/Morse_code.
    var morseCodeDictionary = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
    };

    // Change letters to lowercase.
    str = str.toLowerCase()
    
    // Strip all characters except numbers, letters, and spaces.
    // TODO: This needs to be tested with accented characters.
    str = str.replace(/[^0-9a-z\s]/gi, '');

    // For each character in the Morse Code dictionary, replace all occurences
    // in the string with their Morse Code equivalent.
    Object.entries(morseCodeDictionary).forEach(function([key, value]) {
        var re = new RegExp(key, 'g');
        str = str.replace(re, value); 
    });

    // Return the converted string.
    return str;
}
