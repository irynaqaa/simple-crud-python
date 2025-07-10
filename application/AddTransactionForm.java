import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.DatePicker;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextField;
import javafx.scene.control.ToggleGroup;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class AddTransactionForm extends Application {

    @Override
    public void start(Stage primaryStage) {
        // Create form fields
        TextField amountField = new TextField();
        ComboBox<String> categoryComboBox = new ComboBox<>();
        DatePicker dateField = new DatePicker();
        TextField descriptionField = new TextField();
        ToggleGroup typeToggleGroup = new ToggleGroup();
        RadioButton incomeRadioButton = new RadioButton("Income");
        incomeRadioButton.setToggleGroup(typeToggleGroup);
        RadioButton expenseRadioButton = new RadioButton("Expense");
        expenseRadioButton.setToggleGroup(typeToggleGroup);

        // Create form layout
        VBox formLayout = new VBox(10);
        formLayout.setPadding(new Insets(10));
        formLayout.setAlignment(Pos.CENTER);
        formLayout.getChildren().addAll(
                new Text("Amount:"),
                amountField,
                new Text("Category:"),
                categoryComboBox,
                new Text("Date:"),
                dateField,
                new Text("Description:"),
                descriptionField,
                new Text("Type:"),
                incomeRadioButton,
                expenseRadioButton
        );

        // Create submit button
        Button submitButton = new Button("Submit");
        formLayout.getChildren().add(submitButton);

        // Create scene and stage
        Scene scene = new Scene(formLayout, 300, 400);
        primaryStage.setTitle("Add Transaction");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}