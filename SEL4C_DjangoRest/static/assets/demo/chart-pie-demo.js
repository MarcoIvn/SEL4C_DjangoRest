// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var gender_labels = ctx.getAttribute("data-labels");
var gender_data = ctx.getAttribute("data-data")

gender_labels = JSON.parse(gender_labels);
gender_data = JSON.parse(gender_data);
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: gender_labels,
    datasets: [{
      data: gender_data,
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745'],
    }],
  },
});
