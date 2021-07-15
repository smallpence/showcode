//
// Created by sam on 14/03/2021.
//

class Node {
public:
    Node* sibling;
    Node* children;
    char numChildren;
    char value;

    Node() {
        sibling = nullptr;
        children = nullptr;
        numChildren = 0;
    }

    void addChild(Node newNode) {
        Node* tempChild = children;

        if (tempChild == nullptr) tempChild = &newNode;

        while (tempChild->sibling != nullptr) {
//            Node child = *tempChild;
//            tempChild = child.sibling;
            tempChild = tempChild->sibling;
        }

        tempChild->sibling = &newNode;
        numChildren++;
    }

    Node* findChild(char value) {
        if (numChildren == 0) return nullptr;


    }
};

class Tree {
public:
    Node root;
    char numNodes;


};

