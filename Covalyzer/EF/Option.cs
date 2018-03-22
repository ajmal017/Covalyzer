namespace Covalyzer.Ef
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    [Table("Option")]
    public partial class Option
    {
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public int id { get; set; }

        public int security_id { get; set; }

        public int underlyer_id { get; set; }

        public int expiry_date_id { get; set; }

        [StringLength(50)]
        public string strike { get; set; }

        public int? open_interest { get; set; }

        public virtual ExpiryDate ExpiryDate { get; set; }

        public virtual Security Security { get; set; }

        public virtual Security Security1 { get; set; }
    }
}
