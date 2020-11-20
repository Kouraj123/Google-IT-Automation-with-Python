#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails
import os
def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sales={"sales":0}
  years={}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    item_sales=item["total_sales"]
    if item_sales>max_sales["sales"]:
      item["sales"]=item_sales
      max_sales=item
    if item["car"]["car_year"] not in years:
      years[item["car"]["car_year"]]=1
    else:
      years[item["car"]["car_year"]]+=1
    # TODO: also handle max sales
    # TODO: also handle most popular car_year

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
  ]
  summary.append("The {} had the most sales: {}".format(format_car(max_sales["car"]), max_sales["sales"]))
  max_count=max(years.values())
  year=0
  sale_count=0
  for k in years:
   if years[k]==max_count:
    year=k
  for item in data:
   if item["car"]["car_year"]==year:
    sale_count+=item["total_sales"]
  summary.append("The most popular year was {} with {} sales".format(year, sale_count))
  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  print(summary)
  # TODO: turn this into a PDF report
  reports.generate("/tmp/cars.pdf",summary[0]+"<br/>"+summary[1]+"<br/>"+summary[2],"sales summary",cars_dict_to_table(data))
  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = summary[0]+"\n"+summary[1]+"\n"+summary[2]
  message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
  emails.send(message)


if __name__ == "__main__":
  main(sys.argv)