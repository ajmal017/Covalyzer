namespace Covalyzer.EF
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    [Table("Day")]
    public partial class Day
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
        public Day()
        {
            EarningcallsDate = new HashSet<EarningcallsDate>();
            ExDividendDate = new HashSet<ExDividendDate>();
            ExpiryDate = new HashSet<ExpiryDate>();
        }

        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public int id { get; set; }

        [Column("day", TypeName = "date")]
        public DateTime? day1 { get; set; }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<EarningcallsDate> EarningcallsDate { get; set; }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<ExDividendDate> ExDividendDate { get; set; }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<ExpiryDate> ExpiryDate { get; set; }
    }
}
