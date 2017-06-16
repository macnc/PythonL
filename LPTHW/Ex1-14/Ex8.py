#!/use/bin/
# _*_coding: utf-8


# Define a formatter variable and set four characters
# Formatter replaced symble '%r' in it.
formatter = "%r %r %r %r"

# print out formatter variables with numbers, strings, bools
# And formatter itself values for replacing format charactor
# in it.
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I siad goodnight."
)

# print out original value if formatter.
print formatter
