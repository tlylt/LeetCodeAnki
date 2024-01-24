/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    ans := [][]int{}
    if root == nil {
        return ans
    }
    
    queue := list.New()
    queue.PushBack(root)
    
    for queue.Len() > 0 {
        level := make([]int, 0)
        l := queue.Len()
        for i := 0; i < l; i++ {
            curr := queue.Remove(queue.Front()).(*TreeNode)
            if curr.Left != nil {
                queue.PushBack(curr.Left)
            }
            if curr.Right != nil {
                queue.PushBack(curr.Right)
            }
            level = append(level, curr.Val)
        }
        ans = append(ans, level)
    }
    return ans
}