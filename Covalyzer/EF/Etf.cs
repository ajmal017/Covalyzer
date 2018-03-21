namespace Covalyzer.EF
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    [Table("Etf")]
    public partial class Etf
    {
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public int id { get; set; }

        public int security_id { get; set; }

        public int exdividend_dates_id { get; set; }

        public virtual ExDividendDate ExDividendDate { get; set; }

        public virtual Security Security { get; set; }
    }
}
