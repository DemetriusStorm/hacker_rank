/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
  let reversed = '';
    try {
      s.split();
      for (let i = 0; i < s.length; i += 1) {
        const currentChar = s[i];
        reversed = `${currentChar}${reversed}`;
      }
      console.log(reversed);
    }
    catch (e) {
      console.log(e.message);
      console.log(s);
    }
}
