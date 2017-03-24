title <- commandArgs(trailingOnly = TRUE)[1]

# Draw and save numbers from the standard normal distribution
set.seed(10)
x <- rnorm(10)
write.table(x, file = title, col.names = 'Values', sep = '|')
