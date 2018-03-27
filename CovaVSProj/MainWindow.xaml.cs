using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Data.Entity;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace CovaVSProj
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public Stock newStock { get; set; }
        public Option newOption { get; set; }

        CovalyzerEntities context = new CovalyzerEntities();
        CollectionViewSource stockViewSource;
        CollectionViewSource optionViewSource;

        public MainWindow()
        {
            InitializeComponent();
            newStock = new Stock();
            newOption = new Option();
            stockViewSource = ((CollectionViewSource)
                (FindResource("stockViewSource")));
            //optionViewSource = ((CollectionViewSource)
            //    (FindResource("optionViewSource")));
            DataContext = this;
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {

            //System.Windows.Data.CollectionViewSource stockViewSource = ((System.Windows.Data.CollectionViewSource)(this.FindResource("stockViewSource")));
            // Load data by setting the CollectionViewSource.Source property:
            // stockViewSource.Source = [generic data source]
            //System.Windows.Data.CollectionViewSource optionViewSource = ((System.Windows.Data.CollectionViewSource)(this.FindResource("optionViewSource")));
            // Load data by setting the CollectionViewSource.Source property:
            // optionViewSource.Source = [generic data source]
            context.Stock.Load();            
            context.Option.Load();
            context.Security.Load();

            // After the data is loaded call the DbSet<T>.Local property    
            // to use the DbSet<T> as a binding source.   
            stockViewSource.Source = context.Stock.Local;
        }
        private void LastCommandHandler(object sender, ExecutedRoutedEventArgs e)
        {
            stockViewSource.View.MoveCurrentToLast();
        }

        private void PreviousCommandHandler(object sender, ExecutedRoutedEventArgs e)
        {
            stockViewSource.View.MoveCurrentToPrevious();
        }

        private void NextCommandHandler(object sender, ExecutedRoutedEventArgs e)
        {
            stockViewSource.View.MoveCurrentToNext();
        }

        private void FirstCommandHandler(object sender, ExecutedRoutedEventArgs e)
        {
            stockViewSource.View.MoveCurrentToFirst();
        }
        private void DeleteStockCommandHandler(object sender, ExecutedRoutedEventArgs e)
        {
            // If existing window is visible, then delete the customer and all their orders.  
            // In a real application, you should add warnings and allow a user to cancel the operation.  
            var cur = stockViewSource.View.CurrentItem as Stock;

            var stock = (from c in context.Stock
                         where c.id == cur.id
                         select c).FirstOrDefault();

            if (stock != null)
            {
                //foreach (var opt in stock.Security.Option.ToList())
                //{
                //    Delete_Option(opt);
                //}
                context.Stock.Remove(stock);
            }
            context.SaveChanges();
            stockViewSource.View.Refresh();
        }
        private void UpdateCommandHandler(object sender, ExecutedRoutedEventArgs e)
        {
            if (newStockGrid.IsVisible)
            {
                // Create a new object because the old one  
                // is being tracked by EF now.  
                newStock = new Stock();
                newStock.name = add_companyNameTextBox.Text;
                //    newStock.City = add_cityTextBox.Text;
                //    newStock.CompanyName = add_companyNameTextBox.Text; 
                //    newStock.ContactName = add_contactNameTextBox.Text;
                //    newStock.ContactTitle = add_contactTitleTextBox.Text;
                //    newStock.Country = add_countryTextBox.Text;
                //    newStock.StockID = add_customerIDTextBox.Text;
                //    newStock.Fax = add_faxTextBox.Text;
                //    newStock.Phone = add_phoneTextBox.Text;
                //    newStock.PostalCode = add_postalCodeTextBox.Text;
                //    newStock.Region = add_regionTextBox.Text;

                //    // Perform very basic validation  
                if (newStock.id <= 50)
                {
                    // Insert the new customer at correct position:  
                    int len = context.Stock.Local.Count();
                    int pos = len;
                    for (int i = 0; i < len; ++i)
                    {
                        if (String.CompareOrdinal(newStock.id.ToString(), context.Stock.Local[i].id.ToString()) < 0)
                        {
                            pos = i;
                            break;
                        }
                    }
                    context.Stock.Local.Insert(pos, newStock);
                    stockViewSource.View.Refresh();
                    stockViewSource.View.MoveCurrentTo(newStock);
                }
                else
                {
                    MessageBox.Show("StockID must have 5 characters.");
                }

                newStockGrid.Visibility = Visibility.Collapsed;
                existingStockGrid.Visibility = Visibility.Visible;
            }
            else if (newOptionGrid.IsVisible)
            {
                // Order ID is auto-generated so we don't set it here.  
                // For StockID, address, etc we use the values from current customer.  
                // User can modify these in the datagrid after the order is entered.  

                //newOption.OrderDate = add_orderDatePicker.SelectedDate;
                //newOrder.RequiredDate = add_requiredDatePicker.SelectedDate;
                //newOrder.ShippedDate = add_shippedDatePicker.SelectedDate;
                //    try
                //    {
                //        // Exercise for the reader if you are using Northwind:  
                //        // Add the Northwind Shippers table to the model.  
                //        // Acceptable ShipperID values are 1, 2, or 3.  
                //        if (add_ShipViaTextBox.Text == "1" || add_ShipViaTextBox.Text == "2"
                //            || add_ShipViaTextBox.Text == "3")
                //        {
                //            newOrder.ShipVia = Convert.ToInt32(add_ShipViaTextBox.Text);
                //        }
                //        else
                //        {
                //            MessageBox.Show("Shipper ID must be 1, 2, or 3 in Northwind.");
                //            return;
                //        }
                //    }
                //    catch
                //    {
                //        MessageBox.Show("Ship Via must be convertible to int");
                //        return;
                //    }
                //    try
                //    {
                //        newOrder.Freight = Convert.ToDecimal(add_freightTextBox.Text);
                //    }
                //    catch
                //    {
                //        MessageBox.Show("Freight must be convertible to decimal.");
                //        return;
                //    }

                //    // Add the order into the EF model  
                //    context.Orders.Add(newOrder);
                //    ordViewSource.View.Refresh();
            }

            // Save the changes, either for a new customer, a new order  
            // or an edit in an existing customer or order  
            context.SaveChanges();
        }
        private void Delete_Option(Option option)
        {
            // Find the order in the EF model.  
            var opt = (from o in context.Option.Local
                       where o.id == option.id
                       select o).FirstOrDefault();

            // Delete all the order_details that have  
            // this Order as a foreign key  
            //foreach (var detail in opt.ExpiryDate.Day.ToList())
            //{
            //    context.Order_Details.Remove(detail);
            //}

            // Now it's safe to delete the order.  
            context.Option.Remove(opt);
            context.SaveChanges();

            // Update the data grid.  
            //optionViewSource.View.Refresh();
        }
    }
}
