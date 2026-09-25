# Step 1: the raw text (triple-quoted, since it spans multiple lines)
summary = """Frontend Developer with 5 years of experience designing and developing scalable, high-performance web applications
using React.js, Redux, JavaScript (ES6+) and modern frontend technologies. Experienced in building reusable com-
ponent architectures, interactive dashboards, real-time data visualization, secure authentication, and REST API inte-
grations. Proven ability to optimize application performance, improve user experience, and deliver production-ready
solutions in Agile environments while collaborating with cross-functional teams."""

# Step 2: clean it into one continuous, lowercase line of words
clean = summary.replace("-\n", "").replace("\n", " ").lower()

# Step 3: split into a list of individual words
words = clean.split()

# Step 4: count occurrences of each word into a dict
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

# Step 5: sort the (word, count) pairs by count, highest first
sorted_words = sorted(counts.items(), key=lambda item: item[1], reverse=True)

# Step 6: print the top 5
top5 = sorted_words[:5]
for word, count in top5:
    print(word, count)


# Walking through why each step exists:

# Step 1 stores your resume paragraph as one string. It has to be triple-quoted (""") rather than single-quoted, because the text has real line breaks in it — regular "..." strings can't contain those, which is the exact error you hit a few messages ago.

# Step 2 fixes two problems with the raw text before we can count words properly: the hyphenated line-break words like "com-\nponent" get glued back into "component" first (order matters here — this has to run before the plain "\n" replace, or you'd end up with "com- ponent" instead), then remaining line breaks become spaces so the whole thing reads as one line. .lower() at the end makes sure "Frontend" and "frontend" count as the same word instead of two different dict keys.

# Step 3 turns that one long string into a list of individual words — .split() with no arguments splits on any whitespace and throws away the empty pieces, so you get a clean list like ["frontend", "developer", "with", "5", "years", ...].

# Step 4 is the counting logic from a couple messages ago — counts.get(word, 0) returns the word's existing count, or 0 if it's never been seen, then adds 1 and stores it back. After this loop, counts is a dict mapping every unique word to how many times it appeared.

# Step 5 turns that dict into a sorted list of (word, count) tuples, ranked by count descending — key=lambda item: item[1] tells sorted() to compare by the count (index 1 of each tuple) rather than the word itself, and reverse=True puts the highest counts first instead of sorted()'s default lowest-first order.

# Step 6 slices off just the first 5 entries and unpacks each (word, count) pair to print it.

# Run this exactly as-is first and check your output — you'll almost certainly see words like "and", "the", "in" dominate the top 5, since short connector words are naturally the most frequent in any paragraph.