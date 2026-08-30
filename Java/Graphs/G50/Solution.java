package Graphs.G50;

import java.util.*;

public class Solution {
    public static List<List<String>> accountsMerge(List<List<String>> arr) {
        Map<Integer, String> nodeIntegerToName = getNameAsIntegerNodes(arr);
        DisjointSet<Integer> disjointSet = new DisjointSet<>(nodeIntegerToName.keySet().stream().toList());
        Map<String, Integer> emailToNodesMappings = new HashMap<>();
        for (int i = 0; i < arr.size(); i += 1) {
            List<String> profile = arr.get(i);
            for (int j = 1; j < profile.size(); j += 1) {
                String email = profile.get(j);
                if (emailToNodesMappings.containsKey(email)) {
                    disjointSet.union(i, emailToNodesMappings.get(email));
                } else {
                    emailToNodesMappings.put(email, i);
                }
            }
        }
        Map<Integer, List<String>> mergedMapOfNodes = getBlankMap(nodeIntegerToName.keySet());
        for (String email : emailToNodesMappings.keySet()) {
            Integer parentNode = emailToNodesMappings.get(email);
            Integer ultimateParentNode = disjointSet.getUltimateParent(parentNode);
            mergedMapOfNodes.get(ultimateParentNode).add(email);
        }
        List<List<String>> result = new ArrayList<>();
        for (Integer node : mergedMapOfNodes.keySet()) {
            List<String> emails = mergedMapOfNodes.get(node);
            String name = nodeIntegerToName.get(node);
            if (!emails.isEmpty()) {
                List<String> row = new ArrayList<>(List.of(name));
                emails.sort(null);
                row.addAll(emails);
                result.add(row);
            }
        }
        return result;
    }

    private static Map<Integer, List<String>> getBlankMap(Set<Integer> integers) {
        Map<Integer, List<String>> result = new HashMap<>();
        for (Integer node : integers) {
            result.put(node, new ArrayList<>());
        }
        return result;
    }

    private static Map<Integer, String> getNameAsIntegerNodes(List<List<String>> arr) {
        Map<Integer, String> result = new HashMap<>();
        for (int i = 0; i < arr.size(); i += 1) {
            result.put(i, arr.get(i).getFirst());
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(
                accountsMerge(
                        Arrays.asList(
                                Arrays.asList("John", "j1", "j2", "j3"),
                                Arrays.asList("John", "j4"),
                                Arrays.asList("Raj", "r1", "r2"),
                                Arrays.asList("John", "j1", "j5"),
                                Arrays.asList("Raj", "r2", "r3"),
                                Arrays.asList("Mary", "m1")
                        )
                )
        );

        System.out.println(
                accountsMerge(
                        Arrays.asList(
                                Arrays.asList("John", "johnsmith@mail.com", "john_newyork@mail.com"),
                                Arrays.asList("John", "johnsmith@mail.com", "john00@mail.com"),
                                Arrays.asList("Mary", "mary@mail.com"),
                                Arrays.asList("John", "johnnybravo@mail.com")
                        )
                )
        );

        System.out.println(
                accountsMerge(
                        Arrays.asList(
                                Arrays.asList("Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"),
                                Arrays.asList("Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"),
                                Arrays.asList("Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"),
                                Arrays.asList("Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"),
                                Arrays.asList("Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co")
                        )
                )
        );
    }
}
