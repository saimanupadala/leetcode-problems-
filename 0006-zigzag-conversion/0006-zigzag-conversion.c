char* convert(char* s, int numRows) {
 if (numRows == 1 || s == NULL)
        return s;

    int len = strlen(s);
    char* result = (char*)malloc(len + 1);

    int idx = 0;
    int cycle = 2 * numRows - 2;

    for (int row = 0; row < numRows; row++) {
        for (int i = row; i < len; i += cycle) {
            result[idx++] = s[i];

            int diag = i + cycle - 2 * row;
            if (row != 0 && row != numRows - 1 && diag < len)
                result[idx++] = s[diag];
        }
    }

    result[idx] = '\0';
    return result;
}
   
