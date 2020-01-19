/*
 * Created by Damon.
 */

#define HASH_TABLE_SIZE 100

struct hash_item {
    int key;
    int value;
    struct hash_item *next;
};



