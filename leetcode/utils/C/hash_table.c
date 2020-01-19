
#include <stdio.h>
#include <stdlib.h>

#include "hash_table.h"

int get_hash_index(int key) {
    key = abs(key);
    return (key % HASH_TABLE_SIZE);
}
