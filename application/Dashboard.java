import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class Dashboard extends Application {

    @Override
    public void start(Stage primaryStage) {
        // Create labels to display total income, total expenses, and balance
        Label totalIncomeLabel = new Label("Total Income: $0.00");
        Label totalExpensesLabel = new Label("Total Expenses: $0.00");
        Label balanceLabel = new Label("Balance: $0.00");

        // Create a button to refresh the dashboard
        Button refreshButton = new Button("Refresh");
        refreshButton.setOnAction(event -> {
            // Calculate and update the dashboard
            calculateDashboard(totalIncomeLabel, totalExpensesLabel, balanceLabel);
        });

        // Create a vertical box layout to arrange the components
        VBox root = new VBox(10);
        root.setPadding(new Insets(10));
        root.setAlignment(Pos.CENTER);
        root.getChildren().addAll(totalIncomeLabel, totalExpensesLabel, balanceLabel, refreshButton);

        // Create a scene and set it to the primary stage
        Scene scene = new Scene(root, 300, 200);
        primaryStage.setTitle("Dashboard");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void calculateDashboard(Label totalIncomeLabel, Label totalExpensesLabel, Label balanceLabel) {
        // Retrieve all income and expense transactions from the database
        double totalIncome = retrieveTotalIncome();
        double totalExpenses = retrieveTotalExpenses();

        // Calculate the balance
        double balance = totalIncome - totalExpenses;

        // Update the labels with the calculated values
        totalIncomeLabel.setText(String.format("Total Income: $%.2f", totalIncome));
        totalExpensesLabel.setText(String.format("Total Expenses: $%.2f", totalExpenses));
        balanceLabel.setText(String.format("Balance: $%.2f", balance));
    }

    private double retrieveTotalIncome() {
        // Implement logic to retrieve total income from the database
        // For demonstration purposes, return a sample value
        return 1000.00;
    }

    private double retrieveTotalExpenses() {
        // Implement logic to retrieve total expenses from the database
        // For demonstration purposes, return a sample value
        return 500.00;
    }

    public static void main(String[] args) {
        launch(args);
    }
}
