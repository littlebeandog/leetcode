水桶的两边分别位于数组的最左和最右.
假设:
- 将外面的板子替换为靠内的某一块板子会增加水桶的容积,那么这块板子的高度一定大于原来的高度
- 被替换的板子一定不是更高的那块, 否则水桶的`weight`减小了但`height`并没有增加

因此将两块板子从最外围向内依次移动,每次让较小的那块移动一步,遍历一次即可.