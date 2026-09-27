library(ggplot2)

data <- na.omit(iris[c("Species", "Petal.Length", "Sepal.Length")])
print(aggregate(cbind(Petal.Length, Sepal.Length) ~ Species, data = data, FUN = mean))

plot <- ggplot(data, aes(Petal.Length, Sepal.Length, color = Species)) +
  geom_point() +
  labs(x = "Petal length (cm)", y = "Sepal length (cm)") +
  theme_minimal()
print(plot)

model <- lm(Sepal.Length ~ Petal.Length, data = data)
print(coef(model))
