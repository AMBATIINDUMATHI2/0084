#include <stdio.h>
#include <stdlib.h>

// Define the structure for a node in the linked list
struct Node 
{
    int data;
    struct Node* next;
};

// Function to create a new node with the given data
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to insert a new node at the beginning of the linked list
struct Node* insertAtBeginning(struct Node* head, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = head;
    return newNode;
}

// Function to insert a new node at the end of the linked list
struct Node* insertAtEnd(struct Node* head, int data) {
    struct Node* newNode = createNode(data);
    if (head == NULL) {
        return newNode;
    }

    struct Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
    return head;
}

// Function to insert a new node at a specific position in the linked list
struct Node* insertAtPosition(struct Node* head, int data, int position) {
    struct Node* newNode = createNode(data);
    if (position == 1) {
        newNode->next = head;
        return newNode;
    }

    struct Node* current = head;
    for (int i = 1; i < position - 1 && current != NULL; i++) {
        current = current->next;
    }

    if (current == NULL) {
        printf("Invalid position\n");
        return head;
    }

    newNode->next = current->next;
    current->next = newNode;
    return head;
}

// Function to delete the first node in the linked list
struct Node* deleteFromBeginning(struct Node* head) {
    if (head == NULL) {
        printf("List is empty\n");
        return NULL;
    }

    struct Node* temp = head;
    head = head->next;
    free(temp);
    return head;
}

// Function to delete the last node in the linked list
struct Node* deleteFromEnd(struct Node* head) {
    if (head == NULL) {
        printf("List is empty\n");
        return NULL;
    }

    if (head->next == NULL) {
        free(head);
        return NULL;
    }

    struct Node* current = head;
    while (current->next->next != NULL) {
        current = current->next;
    }

    free(current->next);
    current->next = NULL;
    return head;
}

// Function to delete a node from a specific position in the linked list
struct Node* deleteAtPosition(struct Node* head, int position) {
    if (head == NULL) {
        printf("List is empty\n");
        return NULL;
    }

    if (position == 1) {
        struct Node* temp = head;
        head = head->next;
        free(temp);
        return head;
    }

    struct Node* current = head;
    for (int i = 1; i < position - 1 && current != NULL; i++) {
        current = current->next;
    }

    if (current == NULL || current->next == NULL) {
        printf("Invalid position\n");
        return head;
    }

    struct Node* temp = current->next;
    current->next = current->next->next;
    free(temp);
    return head;
}

// Function to display all the elements in the linked list
void displayList(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

// Function to search for an element in the linked list and return its position
int searchElement(struct Node* head, int key) {
    int position = 1;
    struct Node* current = head;
    while (current != NULL) {
        if (current->data == key) {
            return position;
        }
        current = current->next;
        position++;
    }
    return -1; // Element not found
}

// Function to update the value of a node at a specific position in the linked list
struct Node* updateElement(struct Node* head, int position, int newData) {
    struct Node* current = head;
    for (int i = 1; i < position && current != NULL; i++) {
        current = current->next;
    }

    if (current == NULL) {
        printf("Invalid position\n");
        return head;
    }

    current->data = newData;
    return head;
}

// Main function to test the linked list implementation
int main() {
    struct Node* head = NULL;

    // Insert elements at the beginning
    head = insertAtBeginning(head, 3);
    head = insertAtBeginning(head, 7);
    head = insertAtBeginning(head, 12);

    // Display the linked list
    printf("Linked List after insertions at the beginning: ");
    displayList(head);

    // Insert elements at the end
    head = insertAtEnd(head, 5);
    head = insertAtEnd(head, 9);

    // Display the linked list
    printf("Linked List after insertions at the end: ");
    displayList(head);

    // Insert at a specific position
    head = insertAtPosition(head, 15, 3);

    // Display the linked list
    printf("Linked List after insertion at position 3: ");
    displayList(head);

    // Delete from the beginning
    head = deleteFromBeginning(head);

    // Display the linked list
    printf("Linked List after deletion from the beginning: ");
    displayList(head);

    // Delete from the end
    head = deleteFromEnd(head);

    // Display the linked list
    printf("Linked List after deletion from the end: ");
    displayList(head);

    // Delete at a specific position
    head = deleteAtPosition(head, 2);

    // Display the linked list
    printf("Linked List after deletion at position 2: ");
    displayList(head);

    // Search for an element
    int key = 5;
    int position = searchElement(head, key);
    if (position != -1) {
        printf("Element %d found at position %d\n", key, position);
    } else {
        printf("Element %d not found in the list\n", key);
    }

    // Update an element at a specific position
    head = updateElement(head, 2, 8);

    // Display the linked list
    printf("Linked List after updating element at position 2: ");
    displayList(head);

    return 0;
}
