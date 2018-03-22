namespace Covalyzer.Ef
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    [Table("Stock")]
    public partial class Stock
    {
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public int id { get; set; }

        public int security_id { get; set; }

        public int exdividend_dates_id { get; set; }

        public int earningcall_dates_id { get; set; }

        [StringLength(10)]
        public string name { get; set; }

        public virtual EarningcallsDate EarningcallsDate { get; set; }

        public virtual ExDividendDate ExDividendDate { get; set; }

        public virtual Security Security { get; set; }
    }
}
