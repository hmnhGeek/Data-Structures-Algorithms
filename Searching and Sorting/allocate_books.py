# Problem link - https://www.naukri.com/code360/problems/allocate-books_1090540
# Solution - https://www.youtube.com/watch?v=Z0hwjftStI4&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=19

def can_be_allocated(books, max_pages, num_students):
    # This function will take O(n) time and O(1) space.

    # assuming that first student has been selected and assigned 0th book.
    students_used = 1
    allocated_pages = books[0]

    # iterate from the 1st index book till the end.
    for i in range(1, len(books)):
        if allocated_pages + books[i] > max_pages:
            # if by adding the current book, the number of pages exceed the limit,
            # increase the student counter and reset the allocated pages to current
            # book, implying that the next student has started holding the book from
            # this index.
            students_used += 1
            allocated_pages = books[i]
        else:
            # otherwise simply add the pages from current book until you are within limits.
            allocated_pages += books[i]

    # if we are able to assign to at most num_students, we return True, otherwise, we return False implying
    # that we need more students to allocate all the books but we have only num_students to allocate.
    return students_used <= num_students


def allocate_books(books, num_students):
    '''
        Allocate books in such a way that:

        1. Each student gets at least one book.
        2. Each book should be allocated to only one student.
        3. Book allocation should be in a contiguous manner.

        You have to allocate the book to ‘num_students’ students such that the maximum number of pages assigned to a
        student is minimum.

        Take example [12, 34, 67, 90] and num_students = 2.
        The bruteforce that we can think of is that we start assuming that each student can hold at max 1 page which
        is not possible because to hold a single book, because even to hold a single book, minimum 12 pages are required.
        Anyway, we continued till 12. At 12, we say that each student can hold at max 12 pages. But again, with this
        scenario, only one student will be able to get a book as all other books have pages > 12.

        Ok! so we continued till 34 pages. At 34, we say that each student can hold at max 34 pages. Although now each
        student will have a book, i.e., one student will have 12 pages book and the other one will have 34 pages one,
        but all the books won't get allocated.

        All the books will be allocated with each student getting at least one book when we start from 90 at the very
        least. Hence, our counter should start from max(books). Basically, we can say that at max 90 pages can be allocated
        so that every student can get a book. Although even in this case, we won't be able to allocate all the books,
        but the idea is to reduce the search space.

        We also need to find an upper limit to our loop. We founded that our counter will start from max(books). The
        worst will happen when a single student gets all the books, i.e., sum(books)? Basically, to find low, we said
        that let's find the maximum number of pages so that all the students can get at least one book. To find high,
        we say that let's find the maximum number of pages so that 1 student gets all the books. In one case, all the
        students are allocated the books and the other all books are allocated.

        Hence, our search space is max(books) to sum(books). Now, if you carefully observe, at max pages = max(books),
        we were not able to allocate all the books. At sum(books) we were not able to allocate to all the students.
        However, there will be some values of the counter where we can allocate all the books to all the students. And,
        we can achieve that by checking that all the books are allocated to all the students or not at each counter value.
        This can be done linearly. If it can be done linearly for increasing number of max pages, we can do it via binary
        search as well.

        Overall time complexity would be thus O(n*log(sum - max)) and O(1) space.
    '''

    # if there are more students than the books, return -1.
    if num_students > len(books):
        return -1

    low = max(books)
    high = sum(books)

    # this will take O(n*log(sum - max)) time and O(1) space.
    while low <= high:
        mid = int(low + (high - low)/2)

        # let us assume that we have mid-number of max pages. Let us check if all the books can be allocated to all
        # the students or not with this set constraint.
        if can_be_allocated(books, mid, num_students):
            # if mid-number of maximum pages can be used to allocate to all the students, let us check for some low
            # mid-value? Because we need to minimize the maximum number of pages, isn't it?
            high = mid - 1
        else:
            low = mid + 1

    # at last, low will be at the point where minimum number of maximum pages can be used to allocate all the books
    # to all the students.
    return low


print(allocate_books([12, 34, 67, 90], 2))
print(allocate_books([25, 46, 28, 49, 24], 4))
print(allocate_books([15, 17, 20], 2))
print(allocate_books([5, 4, 6, 3], 3))
print(allocate_books([2, 3, 1, 1, 1, 1, 1], 5))