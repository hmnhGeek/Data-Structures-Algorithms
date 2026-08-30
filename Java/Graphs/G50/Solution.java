package Graphs.G50;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
                row.addAll(emails);
                result.add(row);
            }
        }
        return result;
    }
}
