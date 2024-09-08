from django.shortcuts import HttpResponse


def book_page(requests):
    response = """
    <h1>Books Lists</h1>   
    
    <ul>
        <li><a href="book/1" style="color: red;">Clean Code</a> </li>
        <li><a href="book/2" style="color: red;">The Pragmatic Programmer</a></li>
        <li><a href="book/3" style="color: red;">Head First Design Patterns</a></li>
        <li><a href="book/4" style="color: red;">Code Complete</a></li>
    </ul>

    """
    return HttpResponse(response)


def first_book(requests):
    response = """
        <h1>Clean Code: A Handbook of Agile Software Craftsmanship</h1> 
        <p><b>Author</b>: Robert Martin</p>
        
        <p>
        
Clean code is a term used to describe computer code that is easy to read, understand, and maintain. Clean code is written in a way that makes it simple, concise, and expressive. It follows a set of conventions, standards, and practices that make it easy to read and follow.

Clean code is free from complexity, redundancy, and other code smells and anti-patterns that can make it difficult to maintain, debug, and modify.

I can't overstate the importance of clean code. When code is easy to read and understand, it makes it easier for developers to work on the codebase. This can lead to increased productivity and reduced errors.

Also, when code is easy to maintain, it ensures that the codebase can be improved and updated over time. This is especially important for long-term projects where code must be maintained and updated for years to come.

        </p>
        
        
        
        
        <a href="../" style="color: red;">Back To List</a
    
    """
    return HttpResponse(response)


def second_book(requests):
    response = """
        <h1>The Pragmatic Programmer: From Journey to Master</h1> 
        <p><b>Authors</b>: Andrew Hunt, David Thomas</p>
        
        <p>
        
 The Pragmatic Programmer: From Journeyman to Master is a book about computer programming and software engineering, written by Andrew Hunt and David Thomas and published in October 1999. It is used as a textbook in related university courses. It was the first in a series of books under the label The Pragmatic Bookshelf. A second edition, The Pragmatic Programmer: Your Journey to Mastery was released in 2019 for the book's 20th anniversary, with major revisions and new material which reflects new technology and other changes in the software engineering industry over the last twenty years.

The book does not present a systematic theory, but rather a collection of tips to improve the development process in a pragmatic way. The main qualities of what the authors refer to as a pragmatic programmer are being an early adopter, to have fast adaptation, inquisitiveness and critical thinking, realism, and being a jack-of-all-trades.

The book uses analogies and short stories to present development methodologies and caveats, for example the broken windows theory, the story of the stone soup, or the boiling frog. Some concepts were named or popularized in the book, such as DRY (or Don't Repeat Yourself) and rubber duck debugging, a method of debugging whose name is a reference to a story in the book.

        </p>        
        
        
        <a href="../" style="color: red;">Back To List</a

    
    """
    return HttpResponse(response)


def third_book(requests):
    response = """
        <h1>Head First Design Patterns: A Brain-Friendly Guide</h1> 
        <p><b>Authors</b>: Eric Freeman, Elisabeth Robson</p>
    
        <p>
        
        What’s so special about design patterns?

        At any given moment, someone struggles with the same software design problems you have. And, chances are, someone else has already solved your problem. This edition of Head First Design Patterns―now updated for Java 8―shows you the tried-and-true, road-tested patterns used by developers to create functional, elegant, reusable, and flexible software. By the time you finish this book, you’ll be able to take advantage of the best design practices and experiences of those who have fought the beast of software design and triumphed.

        What’s so special about this book?

        We think your time is too valuable to spend struggling with new concepts. Using the latest research in cognitive science and learning theory to craft a multi-sensory learning experience, Head First Design Patterns uses a visually rich format designed for the way your brain works, not a text-heavy approach that puts you to sleep.

        </p>
    
        <a href="../" style="color: red;">Back To List</a

    """
    return HttpResponse(response)


def fourth_book(requests):
    response = """
        <h1>Code Complete: A Practical Handbook of Software Construction</h1> 
        <p><b>Author</b>: Steve McConnell</p>
        
        <p>
        
        “An excellent guide to programming style and software construction.”
        —Martin Fowler, Refactoring
        “Steve McConnell’s Code Complete . . . provides a fast track to wisdom for programmers. . . .
        His books are fun to read, and you never forget that he is speaking from hard-won personal
        experience.” —Jon Bentley, Programming Pearls, 2d ed.
        “This is simply the best book on software construction that I've ever read. Every developer
        should own a copy and read it cover to cover every year. After reading it annually for nine
        years, I'm still learning things from this book!”
        —John Robbins, Debugging Applications for Microsoft .NET and Microsoft Windows
        “Today’s software must be robust and resilient, and secure code starts with disciplined software
        construction. After ten years, there is still no better authority than Code Complete.”
        —Michael Howard, Security Engineering, Microsoft Corporation; Coauthor, Writing Secure Code
        “A comprehensive examination of the tactical issues that go into crafting a well-engineered
        program. McConnell’s work covers such diverse topics as architecture, coding standards,
        testing, integration, and the nature of software craftsmanship.”
        —Grady Booch, Object Solutions
        </p>
        
        
        <a href="../" style="color: red;">Back To List</a

    
    """
    return HttpResponse(response)
