# mysql

## 知识点

`undrop-for-innodb`

`SQL恢复`

## 解题

1. 解析Innodb表空间

   ```bash
   ./stream_parser -f /var/lib/mysql/ibdata1
   ```

   数据库页的数据被 stream_parser 储存在文件夹 pages-ibdata1

   现在 InnoDB 表空间的每个 index_id 被保存在单独的文件中。我们可以使用 c_parser 从页中提取记录。但是，我们需要知道什么 index_id 对应表中的 Sakila/actor。我们可以从字典- SYS_TABLES SYS_INDEXES 中获得这些信息。 SYS_TABLES 总 是 储 存 在 文 件 index_id 1 中 ， 即 文 件 页 -ibdata1/FIL_PAGE_INDEX./0000000000000001.page

2. 查找关于 ctf 表的 table_id（ctf）。

3. 

