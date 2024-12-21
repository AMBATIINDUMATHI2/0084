#include <stdio.h>
#include <stdlib.h>

// Node structure for doubly linked list
struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
};

// Global pointer to maintain the head of the list
struct Node* head = NULL;

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}

// Function to insert a node at the beginning of the list
void insertAtBeginning(int data) {
    struct Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
        return;
    }
    newNode->next = head;
    head->prev = newNode;
    head = newNode;
}

// Function to insert a node at the end of the list
void insertAtEnd(int data) {
    struct Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
        return;
    }
    struct Node* temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
    newNode->prev = temp;
}

// Function to insert a node at a specific position in the list
void insertAtPosition(int data, int position) {
    if (position <= 1 || head == NULL) {
        insertAtBeginning(data);
        return;
    }
    struct Node* newNode = createNode(data);
    struct Node* temp = head;
    int count = 1;
    while (count < position - 1 && temp->next != NULL) {
        temp = temp->next;
        count++;
    }
    newNode->next = temp->next;
    if (temp->next != NULL) {
        temp->next->prev = newNode;
    }
    temp->next = newNode;
    newNode->prev = temp;
}

// Function to delete a node at a specific position in the list
void deleteNode(int position) {
    if (head == NULL) {
        return;
    }
    struct Node* temp = head;
    if (position == 1) {
        head = temp->next;
        if (head != NULL) {
            head->prev = NULL;
        }
        free(temp);
        return;
    }
    int count = 1;
    while (temp != NULL && count < position) {
        temp = temp->next;
        count++;
    }
    if (temp == NULL) {
        return;
    }
    if (temp->next != NULL) {
        temp->next->prev = temp->prev;
    }
    temp->prev->next = temp->next;
    free(temp);
}

// Function to search for a node with a specific value
void search(int data) {
    struct Node* temp = head;
    int position = 1;
    while (temp != NULL) {
        if (temp->data == data) {
            printf("%d found at position %d\n", data, position);
            return;
        }
        temp = temp->next;
        position++;
    }
    printf("%d not found in the list\n", data);
}

// Function to update a node at a specific position in the list
void updateNode(int data, int position) {
    struct Node* temp = head;
    int count = 1;
    while (temp != NULL && count < position) {
        temp = temp->next;
        count++;
    }
    if (temp == NULL) {
        return;
    }
    temp->data = data;
}

// Function to display the doubly linked list
void display() {
    struct Node* temp = head;
    printf("Doubly linked list: ");
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    // Inserting elements into the doubly linked list
    insertAtEnd(1);
    insertAtEnd(2);
    insertAtBeginning(0);
    insertAtEnd(3);

    // Printing the doubly linked list
    display();

    // Inserting at a specific position
    insertAtPosition(5, 3);
    display();

    // Deleting a node at a specific position
    deleteNode(2);
    display();

    // Searching for a node
    search(5);

    // Updating a node at a specific position
    updateNode(10, 3);
    display();

    return 0;
}
