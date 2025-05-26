package StacksAndQueues.Problem37;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static String streamFirstNonRepeating(String string) {
        // These will take O(26) space.
        Map<Character, Node<Character>> addressMap = getDefaultAddressMap();
        Map<Character, Boolean> repeatedMap = getDefaultRepeatedMap();

        // create a new doubly linked list.
        DoublyLinkedList<Character> doublyLinkedList = new DoublyLinkedList<>();

        // result string
        StringBuilder stringBuilder = new StringBuilder();

        // loop in the string in O(n) time. All internal operations are O(1).
        for (Character character : string.toCharArray()) {
            // if the character is already repeated, do nothing.
            if (repeatedMap.get(character)) {
                continue;
            }

            // if the character was not yet repeated, and it has been seen second time now, mark it as repeated and,
            // erase it from DLL.
            else if (addressMap.get(character) != null) {
                repeatedMap.put(character, true);
                doublyLinkedList.deleteNode(addressMap.get(character));
            } else {
                // else, add this character in dll and put its address in address map.
                Node<Character> node = doublyLinkedList.push(character);
                addressMap.put(character, node);
            }

            // build the result string.
            if (doublyLinkedList.isEmpty()) {
                stringBuilder.append("#");
            } else {
                stringBuilder.append(doublyLinkedList.getHead().getData());
            }
        }
        return stringBuilder.toString();
    }

    private static Map<Character, Boolean> getDefaultRepeatedMap() {
        String s = "abcdefghijklmnopqrstuvwxyz";
        Map<Character, Boolean> map = new HashMap<>();
        for (Character character : s.toCharArray()) {
            map.put(character, false);
        }
        return map;
    }

    private static Map<Character, Node<Character>> getDefaultAddressMap() {
        String s = "abcdefghijklmnopqrstuvwxyz";
        Map<Character, Node<Character>> map = new HashMap<>();
        for (Character character : s.toCharArray()) {
            map.put(character, null);
        }
        return map;
    }

    public static void main(String[] args) {
        System.out.println(streamFirstNonRepeating("abcbbac"));
        System.out.println(streamFirstNonRepeating("aabc"));
        System.out.println(streamFirstNonRepeating("zz"));
        System.out.println(streamFirstNonRepeating("aabcbc"));
    }
}
