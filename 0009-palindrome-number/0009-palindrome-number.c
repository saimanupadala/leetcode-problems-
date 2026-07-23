bool isPalindrome(int x) {
// Negative numbers and numbers ending in 0 (except 0) are not palindromes
    if (x < 0 || (x % 10 == 0 && x != 0))
        return false;

    int revHalf = 0;

    // Reverse only half of the number
    while (x > revHalf) {
        revHalf = revHalf * 10 + x % 10;
        x /= 10;
    }

    // Check for even or odd digit count
    return (x == revHalf || x == revHalf / 10);
}
    
