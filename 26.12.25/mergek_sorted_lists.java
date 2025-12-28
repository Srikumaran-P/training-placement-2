
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2){
        ListNode dummyNode=new ListNode(-1);
        ListNode temp=dummyNode;
        ListNode t1=list1;
        ListNode t2=list2;
        while(t1!=null && t2!=null){
            if(t1.val<t2.val){
                temp.next=t1;
                temp=t1;
                t1=t1.next;
            }
            else{
                temp.next=t2;
                temp=t2;
                t2=t2.next;
            }
           
        }
         if(t1==null)    temp.next=t2;
         if(t2==null)    temp.next=t1;
         return dummyNode.next;
    }
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists==null || lists.length==0)  return null;
        ListNode head=lists[0];
        for(int i=1;i<lists.length;i++)
            head=mergeTwoLists(head, lists[i]);
        return head;
    }
}
