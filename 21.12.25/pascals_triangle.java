static void pascal(int numRows, List<List<Integer>> list) {
    if (numRows == 0) {
        return;
    }

    pascal(numRows - 1, list);

    List<Integer> innerlist = new ArrayList<>();
    int i = list.size();

    for (int j = 0; j <= i; j++) {
        if (j == 0 || j == i) {
            innerlist.add(1);
        } else {
            List<Integer> prevRow = list.get(i - 1);
            innerlist.add(prevRow.get(j - 1) + prevRow.get(j));
        }
    }

    list.add(innerlist);
}
