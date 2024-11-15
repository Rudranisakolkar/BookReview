from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Review
from .forms import ReviewForm

# View to list all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'reviews/book_list.html', {'books': books})

# View to show details of a single book and its reviews
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    return render(request, 'reviews/book_detail.html', {'book': book, 'reviews': reviews})

# View to add a review for a book
def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form, 'book': book})

# View to edit or delete a review
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        if 'delete' in request.POST:
            review.delete()
            return redirect('book_detail', pk=review.book.pk)
        else:
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('book_detail', pk=review.book.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/edit_review.html', {'form': form, 'review': review})
