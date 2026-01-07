# Write your MySQL query statement below

/*
- Find all the authors that viewed **at least one** of **their own articles**
- Must be sorted in ascending order

For an author to have viewed their own article, they must have the viewer_id
be the same as the author_id.
*/

SELECT DISTINCT author_id as id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC;