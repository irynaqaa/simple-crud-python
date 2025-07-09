/**
 * This class represents a report.
 */
public class Report {
    private Long id;
    private String dateRange;
    private String category;
    private Double amount;

    /**
     * Constructs a new Report instance.
     */
    public Report() {
    }

    /**
     * Gets the ID of the report.
     * @return the ID of the report
     */
    public Long getId() {
        return id;
    }

    /**
     * Sets the ID of the report.
     * @param id the ID to set
     */
    public void setId(final Long id) {
        this.id = id;
    }

    /**
     * Gets the date range of the report.
     * @return the date range of the report
     */
    public String getDateRange() {
        return dateRange;
    }

    /**
     * Sets the date range of the report.
     * @param dateRange the date range to set
     */
    public void setDateRange(final String dateRange) {
        this.dateRange = dateRange;
    }

    /**
     * Gets the category of the report.
     * @return the category of the report
     */
    public String getCategory() {
        return category;
    }

    /**
     * Sets the category of the report.
     * @param category the category to set
     */
    public void setCategory(final String category) {
        this.category = category;
    }

    /**
     * Gets the amount of the report.
     * @return the amount of the report
     */
    public Double getAmount() {
        return amount;
    }

    /**
     * Sets the amount of the report.
     * @param amount the amount to set
     */
    public void setAmount(final Double amount) {
        this.amount = amount;
    }
}

