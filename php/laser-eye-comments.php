<?php
/**
 * Converts a string to Morse Code.
 *
 * @param string $str The string to be converted to Morse Code.
 * @return string The string as Morse Code.
 */
function convertToMorseCode($str)
{
    // See https =>//en.wikipedia.org/wiki/Morse_code.
    $morse_code_dictionary = array(
        'a' => '.-',
        'b' => '-...',
        'c' => '-.-.',
        'd' => '-..',
        'e' => '.',
        'f' => '..-.',
        'g' => '--.',
        'h' => '....',
        'i' => '..',
        'j' => '.---',
        'k' => '-.-',
        'l' => '.-..',
        'm' => '--',
        'n' => '-.',
        'o' => '---',
        'p' => '.--.',
        'q' => '--.-',
        'r' => '.-.',
        's' => '...',
        't' => '-',
        'u' => '..-',
        'v' => '...-',
        'w' => '.--',
        'x' => '-..-',
        'y' => '-.--',
        'z' => '--..',
        '0' => '-----',
        '1' => '.----',
        '2' => '..---',
        '3' => '...--',
        '4' => '....-',
        '5' => '.....',
        '6' => '-....',
        '7' => '--...',
        '8' => '---..',
        '9' => '----.'
    );

    // Change letters to lowercase.
    $str = strtolower($str);
    
    // Strip all characters except numbers, letters, and spaces.
    // TODO: This needs to be tested with accented characters.
    preg_replace('/[^0-9a-z\s]/', '', $str);

    // For each character in the Morse Code dictionary, replace all occurences
    // in the string with their Morse Code equivalent.
    $str = str_replace(array_keys($morse_code_dictionary), array_values($morse_code_dictionary), $str);

    // Return the converted string.
    return $str;
}
