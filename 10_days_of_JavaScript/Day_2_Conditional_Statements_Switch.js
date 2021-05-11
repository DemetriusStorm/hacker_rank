function getLetter(s) {
    let letter;
    // Write your code here
    const firstChar = s[0];
    switch(true) {
      case 'aieou'.includes(firstChar):
        letter = 'A';
        break;
      case 'bcdfg'.includes(firstChar):
        letter = 'B';
        break;
      case 'hjklm'.includes(firstChar):
        letter = 'C';
        break;
      case 'npqrstvwxyz'.includes(firstChar):
        letter = 'D';
        break;
    }
    return letter;
}
