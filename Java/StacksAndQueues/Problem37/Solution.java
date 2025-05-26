package StacksAndQueues.Problem37;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static String streamFirstNonRepeating(String string) {
        Map<Character, Node<Character>> addressMap = getDefaultAddressMap();
        Map<Character, Boolean> repeatedMap = getDefaultRepeatedMap();
        DoublyLinkedList<Character> doublyLinkedList = new DoublyLinkedList<>();
        StringBuilder stringBuilder = new StringBuilder();

        for (Character character : string.toCharArray()) {
            if (repeatedMap.get(character)) {
                continue;
            }
            else if (addressMap.get(character) != null) {
                repeatedMap.put(character, true);
                doublyLinkedList.deleteNode(addressMap.get(character));
            } else {
                Node<Character> node = doublyLinkedList.push(character);
                addressMap.put(character, node);
            }
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
