
#include <cstdio>
#include <cstdlib>

#include "hash_table.hpp"

int get_hash_index(int key) {
    key = std::abs(key);
    return (key % HASH_TABLE_SIZE);
}
