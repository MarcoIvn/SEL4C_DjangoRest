// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Get the JSON data from your HTML attribute
var ctx = document.getElementById("myAreaChart");
var labels = JSON.parse(ctx.getAttribute("data-labels"));
var jsonData = JSON.parse(ctx.getAttribute("data-data"));

// Extract the specific datasets
var dataset1 = jsonData.answers_act1;
var dataset2 = jsonData.answers_act7;

// Define your numeric and description labels
var numeric_labels = labels.answers_int_labels
var description_labels = labels.answers_str_labels

var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: numeric_labels, // Use numeric_labels for X-axis labels
    datasets: [
      {
        label: "Diagnóstico",
        lineTension: 0.3,
        backgroundColor: "rgba(213,184,255,0)",
        borderColor: "rgba(159,90,253,1)",
        pointRadius: 3,
        pointBackgroundColor: "rgba(90,34,139,1)",
        pointBorderColor: "rgba(191,85,236,1)",
        pointHoverRadius: 7,
        pointHoverBackgroundColor: "rgba(140,20,252,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: dataset1,
      },
      {
        label: "Cierre",
        lineTension: 0.3,
        backgroundColor: "rgba(255,213,184,0)",
        borderColor: "rgba(253,159,90,1)",
        pointRadius: 3,
        pointBackgroundColor: "rgba(139,90,34,1)",
        pointBorderColor: "rgba(236,191,85,1)",
        pointHoverRadius: 7,
        pointHoverBackgroundColor: "rgba(252,140,20,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: dataset2,
      },
    ],
  },
  options: {
    scales: {
      xAxes: [
        {
          gridLines: {
            display: true,
          },
          ticks: {
            maxTicksLimit: 100,
            maxRotation: 90, 
            minRotation: 90,
            display: true,
          },
        },
      ],
      yAxes: [
        {
          ticks: {
            min: 0,
            maxTicksLimit: 7,
          },
          gridLines: {
            color: "rgba(0, 0, 0, .125)",
          },
        },
      ],
    },
    legend: {
      display: true, // Display the legend with dataset labels
    },
    tooltips: {
      callbacks: {
        title: function(tooltipItem, data) {
          // Use the description label as the tooltip title
          return description_labels[tooltipItem[0].index];
        },
        label: function(tooltipItem, data) {
          return data.datasets[tooltipItem.datasetIndex].label + ": " + tooltipItem.yLabel;
        },
      },
    },
  },
});
