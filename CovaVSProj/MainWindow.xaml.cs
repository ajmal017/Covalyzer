using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
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
    public MainWindow()
    {
      InitializeComponent();
    }

    private void Window_Loaded(object sender, RoutedEventArgs e)
    {

      System.Windows.Data.CollectionViewSource stockViewSource = ((System.Windows.Data.CollectionViewSource)(this.FindResource("stockViewSource")));
      // Load data by setting the CollectionViewSource.Source property:
      // stockViewSource.Source = [generic data source]
      System.Windows.Data.CollectionViewSource optionViewSource = ((System.Windows.Data.CollectionViewSource)(this.FindResource("optionViewSource")));
      // Load data by setting the CollectionViewSource.Source property:
      // optionViewSource.Source = [generic data source]
    }
  }
}
