int lengthOfLongestSubstring(char* s) {
   int freq[256] = {0};   // ASCII character frequency
    int start = 0, maxLen = 0;

    for (int end = 0; s[end] != '\0'; end++) {
        freq[(unsigned char)s[end]]++;

        // If duplicate found, move start
        while (freq[(unsigned char)s[end]] > 1) {
            freq[(unsigned char)s[start]]--;
            start++;
        }

        int currLen = end - start + 1;
        if (currLen > maxLen)
            maxLen = currLen;
    }

    return maxLen;
}
 
